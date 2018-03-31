angular.module('myApp', ['ngAnimate']);

angular.module('myApp').controller('FormController', FormController);


function FormController($scope) {
	var vm = this;
	$scope.myForm = {};
	vm.step = "one";
	vm.stepTwo = stepTwo;



	function stepTwo(item){
		vm.step = "two";
		vm.reqs = $scope.myForm.requested_amount;
	}
}