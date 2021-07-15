.phony: clean
clean:
	find . -type f -name *.pyc | xargs rm -rf
	find . -type d -name *pycache* | xargs rm -rf

