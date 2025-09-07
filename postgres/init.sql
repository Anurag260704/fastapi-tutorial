-- PostgreSQL initialization script for FastAPI Tutorial
-- This script optimizes the database for development use

-- Create database if not exists (handled by POSTGRES_DB env var)
-- But we can add additional optimizations here

-- Create extensions that might be useful
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Optimize for development environment
-- These settings will be applied to the specific database
ALTER DATABASE "fastapi-tutorial" SET shared_preload_libraries = '';
ALTER DATABASE "fastapi-tutorial" SET log_statement = 'none';
ALTER DATABASE "fastapi-tutorial" SET log_min_duration_statement = 1000;

-- Create indexes for better performance (if needed by your models)
-- These will be created after your tables are created by SQLAlchemy

-- You can add more database-specific optimizations here
-- For example, setting up specific users, permissions, etc.

-- Log completion
DO $$
BEGIN
    RAISE NOTICE 'FastAPI Tutorial database initialization completed successfully!';
END $$;
