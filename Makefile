
main_image := oaze-api-mock:latest

.PHONY: build
build:
	docker build --tag $(main_image) .

.PHONY: run
run:
	docker-compose --project-name oaze-api-mock up

# CLEANING
# =======================================================
.PHONY: clean-images
clean-images:
	docker rmi --force $(main_image)
