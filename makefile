.PHONY: test
test: ## Run tests using Molecule
	molecule test

.PHONY: lint
lint: yamllint ansible-lint

.PHONY: yamllint
yamllint:
	yamllint .

.PHONY: ansible-lint
ansible-lint:
	ansible-lint .
