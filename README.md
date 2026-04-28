# OSPO CERTH Website

Source for the [CERTH Open Source Program Office](https://ospo-certh.github.io/OSPO_CERTH/) website,
built with [Quarto](https://quarto.org/).

## Setup

Install [conda](https://docs.conda.io/en/latest/miniconda.html) or
[mamba](https://mamba.readthedocs.io/en/latest/installation.html), then:

```bash
conda env create -f environment.yml
conda activate ospo-certh
```

## Usage

| Command | Description |
|---|---|
| `quarto preview` | Start a live-reloading local server at `http://localhost:4848` |
| `quarto render` | Build the static site into `_site/` |
