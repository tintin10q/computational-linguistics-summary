build:
	rm -rfv dist
	mkdir -p ./dist
	emanote gen ./dist
