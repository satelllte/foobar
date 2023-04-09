# Google Foobar

My solutions for [Google Foobar](https://foobar.withgoogle.com/) secret coding challenge.

<img src="./static/foobar.png">

## Challenges list

| Year | Level | Name | Source Code |
|---|---|---|---|
| 2022 | 1 | Solar Doomsday | [source](./src/year_2022/level_1/solar_doomsday) |
| 2022 | 2 | Elevator Maintenance | [source](./src/year_2022/level_2/elevator_maintenance) |
| 2022 | 2 | Ion Flux Relabeling | [source](./src/year_2022/level_2/ion_flux_relabeling) |
| 2022 | 3 | Bomb Baby | [source](./src/year_2022/level_3/bomb_baby) |
| 2022 | 3 | Doomsday Fuel | [source](./src/year_2022/level_3/doomsday_fuel) |
| 2022 | 3 | Fuel Injection Perfection | [source](./src/year_2022/level_3/fuel_injection_perfection) |
| 2022 | 3 | Prepare The Bunnies Escape | [source](./src/year_2022/level_3/prepare_the_bunnies_escape) |
| 2022 | 4 | Distract The Trainers | [source](./src/year_2022/level_4/distract_the_trainers) |
| 2022 | 4 | Escape Pods | [source](./src/year_2022/level_4/escape_pods) |
| 2022 | 5 | Dodge The Lasers | [source](./src/year_2022/level_5/dodge_the_lasers) |

## Development

The project uses [Python](https://www.python.org/) programming language for the solutions, so it's needed to be installed first. To make sure it's installed, run:

```sh
python --version
```

Then, install Python dependencies of the project:

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run tests:

```sh
pytest -v
```

**Note about folder structure:**

The unit-tested solutions put into `src` folder, but the ones which aren't, they're just temporary placed into `untested` folder. But regardless of where they're placed here they all were verified inside Google Foobar's terminal.
