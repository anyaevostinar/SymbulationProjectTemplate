# Cookiecutter Symbulation Project

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Symbulation Project.


* GitHub repo: https://github.com/anyaevostinar/SymbulationProjectTemplate/
* Free software: MIT LICENSE

An offshoot of the [Symbulation C++ Library](https://github.com/anyaevostinar/SymbulationEmp).

## Features

* [GitHub Actions](https://github.com/features/actions): Ready for Continuous Integration testing and deployment with GitHub actions.
* [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation and deployment with, for example, [ReadTheDocs](https://readthedocs.io/).

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet::
```bash
pip install -U cookiecutter
```

Generate an Empirical project:
```bash
cookiecutter https://github.com/anyaevostinar/SymbulationProjectTemplate.git
```

`hooks/post_gen_project.sh` will run to initialize submodules.
If you want your repo to automatically push to github, set up the remote repo first.

Take it for a spin!
```bash
make test
```

Then add the repo to your [ReadTheDocs](https://readthedocs.io/) account + turn on the ReadTheDocs service hook.
