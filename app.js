var app = angular.module('app', [])

app.controller('playerController', function($scope) {
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

app.controller('championController', function($scope) {
	$scope.sortType = 'name';
	$scope.sortReverse = false;

	$scope.champions = [

		{name: 'Azir', role: 'Mage', lane: 'Mid', counters: ['Ziggs', 'Talon', 'Xerath'],
			items: ['Sorcerer\'s Shoes', 'Athene\'s Unholy Grail', 'Rabadon\'s Deathcap'],
			abilities: ['Shurima\'s Legacy', 'Conquering Sands', 'Arise!', 'Shifting Sands',
						'Emperor\'s Divide']},

		{name: 'Ezreal', role: 'Adc', lane: 'Bot', counters: ['Draven', 'Graves', 'Miss Fortune'],
			items: ['Berserker\'s Greaves', 'Trinity Force', 'Bloodthirster'],
			abilities: ['Rising Spell Force', 'Mystic Shot', 'Essence Flux', 'Arcane Shift',
						'Trueshot Barrage']},

		{name: 'Ekko', role: 'Mage', lane: 'Mid', counters: ['LeBlanc', 'Cho\'Gath', 'Diana'],
			items: ['Luden\'s Echo', 'Sorcerer\'s Shoes', 'Lich Bane'],
			abilities: ['Z-Drive Resonance', 'Timewinder', 'Parallel Convergence', 'Phase Dive',
						'Chronobreak']}
	];
});