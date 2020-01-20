VECTORS_URL = http://www.ii.uni.wroc.pl/~prych/nlp/poleval_base_vectors.txt

download:
	wget $(VECTORS_URL)

.PHONY: download

VECTORS_FILENAME = poleval_base_vectors.txt

clean:
	rm -vf $(VECTORS_FILENAME)

.PHONY: clean
