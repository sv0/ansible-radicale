.PHONY: test
test:  # Run tests using Molecule
	molecule test

.PHONY: lint
lint: yamllint ansible-lint

.PHONY: yamllint
yamllint:
	yamllint .

.PHONY: ansible-lint
ansible-lint:
	ansible-lint .

.PHONY: release
VERSION?=minor
# target: release - Bump version
release:
	@pip install bumpversion
	@bumpversion $(VERSION)
	@git checkout master
	@git merge devel
	@git checkout devel
	@git push --all
	@git push --tags

.PHONY: minor
minor: release

.PHONY: patch
patch:
	make release VERSION=patch

.PHONY: major
major:
	make release VERSION=major
