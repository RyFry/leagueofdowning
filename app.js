angular.module('app', [])

.controller('playerController', function($scope) {
	$scope.sortType = 'name';
	$scope.sortReverse = false;

	$scope.players = [

		{name: 'Bjergsen', age: 19, position: "mid", totalWins: 9, seasonWins: 9, 
			seasonLosses: 3, team: "TSM", avgKDA: 4.7, avgGPM: 308, avgTotalGold: 18000,
			champions: ['Azir', 'Ezreal', 'Ekko']},

		{name: 'Doublelift', age: 21, position: "adc", totalWins: 7, seasonWins: 7, 
			seasonLosses: 5, team: "CLG", avgKDA: 4.1, avgGPM: 426, avgTotalGold: 16000,
			champions: ['Ashe', 'Sivir', 'Kalista']},

		{name: 'Balls', age: 21, position: "top", totalWins: 3, seasonWins: 3, 
			seasonLosses: 9, team: "C9", avgKDA: 1.8, avgGPM: 301, avgTotalGold: 11000,
			champions: ['Fizz', 'Maokai', 'Rumble']}
	];
});