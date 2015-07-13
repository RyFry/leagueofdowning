angular.module('items', [])

.controller('itemController', function($scope) {
	$scope.sortType = 'name';
	$scope.sortReverse = false;

	$scope.items = [

		{name: 'Sorcerer\'s Shoes', stats: ['+15 Magic Penetration'], recFor: 'Mage',
			cost: 1100, recipe: ['Boots of Speed']},

		{name: 'Athene\'s Unholy Grail', stats: ['+60 Ability Power', '+25 Magic Resist',
												'+20% Cooldown Reduction', '+100% Base Mana Regen'],
			recFor: 'Mage', cost: 2700, recipe: ['Fiendish Codex', 'Chalice ofHarmony']},

		{name: 'Rabadon\'s Deathcap', stats: ['+120 Ability Power'], recFor: 'Mage',
			cost: 3300, recipe: ['Blasting Wand', 'Needlessly Large Rod']},
	];
});