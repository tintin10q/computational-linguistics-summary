pdf:
	python3 merge.py

clean:
	rm -r EXPORT

emanote:
	rm -rfv dist
	mkdir -p ./dist
	emanote gen ./dist
