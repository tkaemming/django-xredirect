# django-xredirect

A simple Django middleware that converts all HTTP 301/302 responses for XHR
requests into HTTP 200 responses with an extra `X-Redirect` header.

This is especially helpful when implementing
"[pjax](http://www.github.com/tkaemming/django-pjax/)"-based applications
without having to completely change an application's urlconf to avoid redirects.

## Installation

Add `xredirect.middleware.XRedirectMiddleware` to your `MIDDLEWARE_CLASSES` in
your Django application settings.
