angular.module('app', [])

.controller('roleController', function($scope) {
	$scope.sortType = 'name';
	$scope.sortReverse = false;

	$scope.roles = [
		{name: 'foo', champions: 'xyz'},
		{name: 'bar', champions: 'zyx'}
	];
});