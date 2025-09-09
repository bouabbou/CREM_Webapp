#!/usr/bin/env python3
"""
PostgreSQL Migration Script for CREM Webapp

This script helps migrate from SQLite to PostgreSQL.
Run with: python migrate_to_postgres.py
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, check=True):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr

def check_postgresql_connection():
    """Check if PostgreSQL is available and accessible"""
    print("Checking PostgreSQL connection...")
    
    # Test basic PostgreSQL connection
    code, stdout, stderr = run_command("psql --version", check=False)
    if code != 0:
        print("✗ PostgreSQL client not found. Please install PostgreSQL first.")
        print("See POSTGRES_MIGRATION.md for installation instructions.")
        return False
    
    print("✓ PostgreSQL client found")
    return True

def create_backup():
    """Create a backup of the current SQLite database"""
    print("Creating SQLite database backup...")
    
    backup_file = "datadump.json"
    if Path(backup_file).exists():
        print(f"! Backup file {backup_file} already exists")
        response = input("Overwrite? (y/N): ").lower().strip()
        if response != 'y':
            print("Using existing backup file")
            return True
    
    command = [
        "python", "manage.py", "dumpdata",
        "--natural-foreign", "--natural-primary",
        "-e", "contenttypes", "-e", "auth.Permission",
        "--indent", "2",
        "--output", backup_file
    ]
    
    code, stdout, stderr = run_command(" ".join(command))
    if code == 0:
        print(f"✓ Backup created: {backup_file}")
        return True
    else:
        print(f"✗ Backup failed: {stderr}")
        return False

def test_postgresql_settings():
    """Test PostgreSQL configuration"""
    print("Testing PostgreSQL settings...")
    
    # Test if production settings can be imported
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CREM_Webapp.production_settings')
        from django.conf import settings
        from django.db import connection
        
        connection.ensure_connection()
        print("✓ PostgreSQL connection successful!")
        return True
        
    except Exception as e:
        print(f"✗ PostgreSQL test failed: {e}")
        print("Please check your DATABASE_URL in environment variables")
        return False

def run_migrations():
    """Run Django migrations on PostgreSQL"""
    print("Running migrations on PostgreSQL...")
    
    command = "python manage.py migrate --settings=CREM_Webapp.production_settings"
    code, stdout, stderr = run_command(command)
    
    if code == 0:
        print("✓ Migrations completed successfully")
        return True
    else:
        print(f"✗ Migrations failed: {stderr}")
        return False

def load_data():
    """Load data into PostgreSQL"""
    print("Loading data into PostgreSQL...")
    
    if not Path("datadump.json").exists():
        print("✗ Backup file not found. Please create a backup first.")
        return False
    
    command = "python manage.py loaddata datadump.json --settings=CREM_Webapp.production_settings"
    code, stdout, stderr = run_command(command)
    
    if code == 0:
        print("✓ Data loaded successfully")
        return True
    else:
        print(f"✗ Data loading failed: {stderr}")
        return False

def verify_migration():
    """Verify that migration was successful"""
    print("Verifying migration...")
    
    # Simple verification by counting records
    verify_script = """
from django.conf import settings
from django.db import connection
from django.contrib.auth.models import User

try:
    connection.ensure_connection()
    user_count = User.objects.count()
    print(f"✓ Migration successful! Found {user_count} users in PostgreSQL")
except Exception as e:
    print(f"✗ Verification failed: {e}")
"""
    
    command = f'python -c "{verify_script}" --settings=CREM_Webapp.production_settings'
    code, stdout, stderr = run_command(command, check=False)
    
    print(stdout)
    if stderr:
        print(f"Stderr: {stderr}")
    
    return code == 0

def main():
    """Main migration function"""
    print("=" * 60)
    print("PostgreSQL Migration Script for CREM Webapp")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Please run this script from the Django project root directory")
        sys.exit(1)
    
    steps = [
        ("Check PostgreSQL connection", check_postgresql_connection),
        ("Create SQLite backup", create_backup),
        ("Test PostgreSQL settings", test_postgresql_settings),
        ("Run migrations", run_migrations),
        ("Load data", load_data),
        ("Verify migration", verify_migration),
    ]
    
    success = True
    for step_name, step_func in steps:
        print(f"\n{'='*50}")
        print(f"Step: {step_name}")
        print(f"{'='*50}")
        
        if not step_func():
            print(f"✗ {step_name} failed")
            success = False
            break
    
    if success:
        print("\n" + "=" * 60)
        print("Migration completed successfully!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Update your production environment to use PostgreSQL")
        print("2. Test your application thoroughly")
        print("3. Consider setting up database backups")
        print("4. Monitor database performance")
    else:
        print("\n❌ Migration failed. Please check the errors above.")
        print("Refer to POSTGRES_MIGRATION.md for troubleshooting.")

if __name__ == "__main__":
    main()