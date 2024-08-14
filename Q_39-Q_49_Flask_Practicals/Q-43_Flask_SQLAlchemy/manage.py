
from app import app, db
from models import User
import click

@app.cli.command('create_db')
def create_db():
    """Create the database and tables."""
    db.create_all()
    click.echo("Database and tables created.")

@app.cli.command('drop_db')
def drop_db():
    """Drop the database and tables."""
    db.drop_all()
    click.echo("Database and tables dropped.")

@app.cli.command('add_user')
@click.argument('username')
@click.argument('email')
@click.argument('password')
def add_user(username, email, password):
    """Add a new user to the database."""
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    click.echo(f"User {username} added.")
