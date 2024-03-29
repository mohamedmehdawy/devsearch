'use strict';

{
  var $ = django.jQuery;

  $.fn.djangoAdminSelect2 = function () {
    $.each(this, function (i, element) {
      $(element).select2({
        ajax: {
          data: function data(params) {
            return {
              term: params.term,
              page: params.page,
              app_label: element.dataset.appLabel,
              model_name: element.dataset.modelName,
              field_name: element.dataset.fieldName
            };
          }
        }
      });
    });
    return this;
  };

  $(function () {
    // Initialize all autocomplete widgets except the one in the template
    // form used when a new formset is added.
    $('.admin-autocomplete').not('[name*=__prefix__]').djangoAdminSelect2();
  });
  $(document).on('formset:added', function () {
    return function (event, $newFormset) {
      return $newFormset.find('.admin-autocomplete').djangoAdminSelect2();
    };
  }(void 0));
}