# A Tool for Predicting Music Success
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

[![License](https://poser.pugx.org/aimeos/aimeos-typo3/license.svg)](https://packagist.org/packages/aimeos/aimeos-typo3)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

> HAMR 2020 Project - https://www.ismir2020.net/hamr/

A python based tool for predicting if a song will appears at Spotify's Top 50 Global ranking based on user inputs.

## Requirements

To run this tool you'll need Python 3. Download Python at https://www.python.org/downloads/.

Also, if you do not have some of the python packages needed a pip command will be executed, so I strongly recommend to have pip installed. Installation guide at https://pip.pypa.io/en/stable/installing/.

## How to use

First, clone this repository with the `git clone` command.

To run the tool basically type

```shell
python predict.py
```
If some of the required python packages are missing, it will first install these packages and then run the tool.

When running the tool you can type three commands as follows:

| Command   | Action                                                      |
| --------- | ----------------------------------------------------------- |
| help      | Prints helpful information for the user                     |
| predict   | Predicts if a song will become popular based on user inputs |
| exit      | Closes the program                                          |
| Other     | If anything else is typed, requests a valid option          |

## Links

My master's thesis where I fully explain the model used in the prediction tool (the text is in Portuguese): https://tede.ufam.edu.br/bitstream/tede/7572/6/Disserta%C3%A7%C3%A3o_CarlosAra%C3%BAjo_PPGI.pdf

My ISMIR 2020 LBD Poster were I also present the model methodology: https://program.ismir2020.net/lbd_433.html

HAMR slides: https://docs.google.com/presentation/d/1u4AJjzmqWdrmm9-l-d4AN4uQFHU3iyYUrKbT4PmaNPI/edit?usp=sharing

Spotify API documentation: https://developer.spotify.com/documentation/
