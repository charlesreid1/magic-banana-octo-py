/**
* ----------------------------------------------------------------------------
* Smoke test: modify css with bootstrap
* ----------------------------------------------------------------------------
*/

define([
  'require',
  'jquery',
  'base/js/events'
 ], function (
    requirejs,
    $,
    events
) {
  'use strict';

  function load_css (name) {
    $('<link/>').attr({
      type: 'text/css',
      rel: 'stylesheet',
      href: requirejs.toUrl(name)
    }).appendTo('head');
  }

  var load_jupyter_extension = function () {
    load_css('./smoke.css');
      /*
    events.on("notebook_loaded.Notebook", do_stuff);
    events.on("kernel_ready.Kernel", do_stuff);
    events.on("output_appended.OutputArea", do_stuff);
    events.on("rendered.MarkdownCell", do_stuff);
    */
  };

  return {
    'load_jupyter_extension': load_jupyter_extension,
    'load_ipython_extension': load_jupyter_extension
  };

});

