angular.module('posAngular')
.directive('numeric', function() {
    return {
      require: 'ngModel',
      link: function (scope, element, attr, ngModelCtrl) {
        function fromUser(text) {
          var transformedInput = text.replace(/[^0-9]/g, '');
          if(transformedInput !== text) {
              ngModelCtrl.$setViewValue(transformedInput);
              ngModelCtrl.$render();
          }
          return transformedInput;  // or return Number(transformedInput)
        }
        ngModelCtrl.$parsers.push(fromUser);
      }
    }
})
.directive('selectAll', function() {
    return function(scope, element, attr) {
      element.on('focus', function(ev) {
        $(this)
          .one('mouseup', function () {
            $(this).select();
            return false;
          })
        .select();
      });

      element.on('keyup', function(ev) {
        if ($(this).val() == '0') {
          $(this).select();
        }
      });
    }
  });

