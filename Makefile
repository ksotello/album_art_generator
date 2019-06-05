
build-client:
	cd client && npm i && npm build
.PHONY: build-client

start-server:
	rm -rf static && mkdir static && FLASK_APP=server/server.py flask run
.PHONY: start-server

start-client:
	cd client && yarn start
.PHONY: start-client

deploy-client:
	make build-client && cd client/build && npx surge --domain album-generator-client.surge.sh
.PHONY: deploy-client

deploy-server:
	cd server && npx surge --domain album-generator-server.surge.sh