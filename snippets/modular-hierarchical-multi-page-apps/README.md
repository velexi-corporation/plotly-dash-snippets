Modular Hierarchical Multi-Page Apps
====================================

_Author(s)_: Kevin Chu `<kevin@velexi.com>`

_Last Updated_: 2022-01-30

------------------------------------------------------------------------------

Contents
--------

1. [Overview][#1]

2. [Architecture][#2]

    2.1. [Callback Structure][#2.1]

    2.2. [Layout Structure][#2.2]

    2.3. [App Structure][#2.3]

    2.4. [Code Structure][#2.4]

3. [Implementation][#3]

    3.1. [Step-by-Step][#3.1]

    3.2. [Recommendations][#3.2]

4. [Future Improvements][#4]

------------------------------------------------------------------------------

## 1. Overview

This snippet demonstrates one method for implementing hierarchical multi-page
apps with a modular code structure. The approach is based on the following
fundamental ideas.

* Use a separate HTML container element for each page (or subpage).

* Use the current URL to determine the active page. When a page becomes active,
  its HTML container is made visible. When a page becomes inactive, its HTML
  container is made invisible.

* Automatically generate callbacks for managing page visibility.

* Use user-defined callbacks triggered when a page's container for a page
  changes visibility to update the page's contents based on its current
  visibility.

* Keep code as modular as possible. Use conventions for code consistency
  across pages. Organize code so that it that reflects the structure of the
  app.

------------------------------------------------------------------------------

## 2. Architecture

### 2.1. Callback Structure

Multi-page navigation and URL routing is implemented using a callback chain
consisting of two core components.

* __URL Router__. This callback updates the visibility of a page's container
  element whenever the URL for the page changes. The `url_route()` function in
  the `utils` module automatically generates this callback.

  Examples:

  ```python
  url_route('section/page_1', 'section-page-1-container')
  url_route('section/page_2', 'section-page-2-container')
  url_route('section', 'section-page-id-container', dynamic_page_id=True)
  ```

* __Page Content Initializers__. These are optional user-defined callbacks that
  dynamically initialize the content of the page when the visibility of a
  page's container changes. The `page_is_active()` function in the `utils`
  module can be used to determine whether a page's content needs to be updated.

  Example:

  ```python
  @app.callback(
      Output('page-dynamic-element', 'children'),
      Input('page-container', component_property='style'),
  )
  def initialize_page(style: str) -> html:
      """
      ...
      """
      # Return empty string if page is inactive
      if not page_is_active(style):
          return ""

      ...
  ```


### 2.2. Layout Structure

* In the root layout for the app, include a `dcc.Location` element to store
  the current URL.

* In the layout for pages with subpages, include a separate HTML container
  element for each subpage. Set the `children` property of each subpage
  container to the page layout for the subpage.

  * _Technical Details_. Each page's visibility is controlled by setting the
    `display` property of the HTML element's CSS style.

* For each page's layout, include only static and/or structural HTML elements.
  For dynamic content, use empty HTML elements that are populated when the
  page's container element becomes visible.

* `app.layout` contains HTML container elements for _all_ pages and subpages.

  * Including all structural elements in `app.layout` allows Dash to perform
    callback validation (without requiring the use of workarounds such as
    `suppress_callback_exception` or `app.validation_layout`).

  * To minimize browser memory usage, page containers with HTML elements
    containing dynamic content should have their `children` or `data`
    properties emptied when not in use. __Note__: HTML elements that serve as
    containers for subpages ___should not___ be dynamically added and removed
    from the app's layout.


### 2.3. App Structure

* `app.py`

  * Contains only the creation of the Dash app

  * Does ___not___ set `app.layout`

* `index.py`

  * Sets `app.layout`

  * Defines all app callbacks by importing the `callbacks` module.

  * Defines all app urls by importing the `urls` module

* `callbacks.py`

  * Defines any callbacks that set dynamic content for HTML elements included
    directly in the app's root layout

  * Defines any callbacks that update the URL based on subpage events

* `layouts.py`

  * Defines functions to return app-level layouts

* `urls.py`

  * Defines URL routes to subpages of the main app


### 2.4. Code Structure

* Organize the code for the pages so that it mirrors the hierarchical structure
  of app's URL structure.

* For each page, include the following files.

  * `__init__.py` (required): makes the page's directory into a Python package
    (so that it can be imported). It should contain the following single line
    (so that the `layouts` module is automatically imported when the package is
    imported).

    ```python
    from . import layouts
    ```

  * `layouts.py` (required): defines all layouts (e.g., page content, menus,
    etc.) for the page.

  * `callbacks.py` (optional): defines the callbacks for the page (e.g., a
    callback to dynamically populate page content). This file is not needed
    for pages with static content (i.e., all of the content is defined in the
    layout).

    * For pages with subpages, this file should import the callback modules
      for the subpages.

      * __Note__. If relative imports are used to import the callback modules
        for subpages, callback modules should be imported using the
        `import ... as` syntax to avoid namespace collisions:

        ```python
        from .subpage import callbacks as subpage_callbacks
        ```

  * `urls.py` (optional): defines URL routes for subpages.

    * For pages whose subpages have subpages, this file should import the urls
      modules for the subpages:

      * __Note__. If relative imports are used to import the urls modules for
        subpages, urls modules should be imported using the `import ... as`
        syntax to avoid namespace collisions:

        ```python
        from .subpage import urls as subpage_urls
        ```

------------------------------------------------------------------------------

## 3. Implementation

### 3.1. Step-by-Step

* Define layout structure as a nested hierarchy of page containers.

  * Make sure that `dcc.Location(id='url', refresh=False)` element is included
    in the root layout.

  * Use nested imports of `layouts.py` modules to ensure that all structural
    components of layouts are included in the full app layout.

* Define URL routes to pages. Use nested imports of `urls.py` modules to ensure
  that all URL routes are constructed.

  * Use the `utils.url_route()` function to set up URL routes.

* Define page callbacks. Use nested imports of `callbacks.py` modules to ensure
  that all callbacks are defined.

  * For pages with content that needs to be dynamically created when the
    becomes visible, define a page content initializer callback that takes the
    `style` component property of the page's container as an input. Use
    `utils.page_is_active()` function to determine whether content needs to be
    updated.

* Set up app.

  * In `app.py`, create the `Dash` app object. Do ___not___ set `app.layout`.

  * In `index.py`,

    * set `app.layout`;

    * register callbacks by importing root-level `callbacks.py` module; and

    * register URL routes by importing root-level `urls.py` module.

### 3.2. Recommendations

* Do ___not___ set `suppress_callback_exceptions=True` when creating `Dash`
  app object. It is better to separate the structural components of a page
  layout from the content. If it is not possible to set `app.layout` so that
  all structural components of the layout are present, use
  `app.validation_layout` to provide a list of all page elements that could
  potenitally be present to Dash when it performs callback validation.

* Avoid changes to the layout that introduce structural changes to the page.

* To reduce the chances of circular import errors, do not automatically
  `urls.py` or `callbacks.py` modules in `__init__.py`.

------------------------------------------------------------------------------

## 4. Future Improvements

* __More Flexible URL Routes__. Expressing URL paths as regular expressions
  would allow URL matching to be more flexible while simplifying the logic
  of URL routers. A possible inspiration for a better URL routing design is
  Django's URL routing implementation.

* __More General URL Parsing Function__. Related to the previous idea, it
  would be useful to have a more general URL parsing function (e.g., based on
  regular expressions) that could be used to support (1) more flexible URL
  routing and (2) a richer URL-based mechanisms to pass parameters (e.g.,
  record ids, API commands, etc.) to callbacks that generate dynamic content
  for pages.

* __Subpage Factory Function or Class__. HTML container elements for subpages
  have a standard structure, so it should be possible to implement a function
  or class that encapsulates creation of subpage layout elements. Having this
  function/class would reduce code redundancy, improve code consistency, and
  reduce the likelihood of errors due to typos.

* __More Modularity of Handling Nested Subpage-Events__. Currently, when the
  contents of an ancestor element are driven by events triggered by a nested
  subpage (e.g., page menu updates), the callback for the ancestor element
  requires knowledge of the entire URL sub-hierarchy. This breaks the
  modularity of the pages at different levels of the URL hierarchy. It would
  be better to develop a mechanism that allows to pass subpage information up
  the URL hierarchy that allows the implementation at different levels of the
  hierarchy to remain more independent of each other.

* __Add Support for 404 Handling__. The URL routing mechanism does not
  currently support 404 errors.

------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview

[#2]: #2-architecture
[#2.1]: #21-callback-structure
[#2.2]: #22-layout-structure
[#2.3]: #23-app-structure
[#2.4]: #24-code-structure

[#3]: #3-implementation
[#3.1]: #31-step-by-step
[#3.2]: #32-recommendations

[#4]: #4-future-improvements
