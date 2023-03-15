


anonymous_filter = lambda word: len([l for l in word if l.lower() == 'я']) > 23

print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))