from datetime import datetime
import click
from owla.owla_connector import DataBase as db

@click.group('customer')
def customer():
    """
    \u001b[34mCustomer\u001b[0m.
    """
    pass

@customer.command("city-ride", short_help = "If your ride type is in the same city.")
def city_ride():
    pick_up = click.prompt("\u001b[36m[+] Enter your pick up location (number from 1 to 10)\u001b[0m", type = int)
    drop = click.prompt("\u001b[36m[+] Enter your drop location (number from 1 to 10)\u001b[0m", type = int)
    when = click.prompt("\u001b[36m[+] Enter 'now' to book a cab now, or enter a later time today (HH:MM:SS)\u001b[0m", type = str)
    click.secho(f"-> The details entered for \033[92mCITY RIDES\033[0m are:\n\t=>The pickup location is: {pick_up}, drop location is: {drop} and time of trip is: {when}", fg = 'blue')

@customer.command("shared-ride", short_help = "If your ride type is shared.")
def shared_ride():
    pick_up = click.prompt("\u001b[36m[+] Enter your pick up location (number from 1 to 10)\u001b[0m", type = int)
    drop = click.prompt("\u001b[36m[+] Enter your drop location (number from 1 to 10)\u001b[0m", type = int)
    when = click.prompt("\u001b[36m[+] Enter 'now' to book a cab now, or enter a later time today (HH:MM:SS)\u001b[0m", type = str)
    click.secho(f"-> The details entered \033[92mSHARED RIDES\033[0m are:\n\t=>The pickup location is: {pick_up}, drop location is: {drop} and time of trip is: {when}", fg = 'blue')

@customer.command("rental-ride", short_help = "If your ride type is rental.")
def rental_ride():
    pick_up = click.prompt("\u001b[36m[+] Enter your pick up location (number from 1 to 10)\u001b[0m", type = int)
    drop = click.prompt("\u001b[36m[+] Enter your drop location (number from 1 to 10)\u001b[0m", type = int)
    when = click.prompt("\u001b[36m[+] Enter 'now' to book a cab now, or enter a later time today (HH:MM:SS)\u001b[0m", type = str)
    click.secho(f"-> The details entered \033[92mRENTAL RIDES\033[0m are:\n\t=>The pickup location is: {pick_up}, drop location is: {drop} and time of trip is: {when}", fg = 'blue')

@customer.command("outstation-ride", short_help = "If your ride type is out of station.")
def outstation_ride():
    pick_up = click.prompt("\u001b[36m[+] Enter your pick up location (number from 1 to 10)\u001b[0m", type = int)
    drop = click.prompt("\u001b[36m[+] Enter your drop location (number from 1 to 10)\u001b[0m", type = int)
    when = click.prompt("\u001b[36m[+] Enter 'now' to book a cab now, or enter a later time today (HH:MM:SS)\u001b[0m", type = str)
    click.secho(f"-> The details entered \033[92mOUTSTATION RIDES\033[0m are:\n\t=>The pickup location is: {pick_up}, drop location is: {drop} and time of trip is: {when}", fg = 'blue')