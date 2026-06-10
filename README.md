# GAAP

German Accident Analytics Platform

## Overview

GAAP is an AI-powered transportation analytics platform built on top of a PostgreSQL accident data warehouse.

The system allows users to ask analytical questions in natural language and receive professional analyst-style reports generated from structured data.

The platform is designed around deterministic analytics and AI-assisted report generation.

## Technology Stack

### Frontend

- Next.js
- JavaScript
- Tailwind CSS
- Framer Motion
- Recharts

### Backend

- FastAPI
- Python

### Database

- PostgreSQL

### AI

- Ollama
- qwen3:8b

## Project Structure

```text
gaap/

backend/
frontend/
database/
etl/
docs/
tests/
data/

README.md
requirements.txt
```

## Supported Analytics

- Counts
- Rankings
- Comparisons
- Trends
- Availability
- Zero Occurrence Queries
- Per Capita Metrics
- Per Vehicle Metrics

## Data Sources

### Accident Records

Unfallorte

2016–2024

### Indicators

- Population
- Vehicle Registrations
- Accident Statistics

### Administrative Data

- Municipalities
- Districts
- States

## AI Responsibilities

### Allowed

- Intent Extraction
- Report Generation

### Not Allowed

- SQL Generation
- Calculations
- Rankings
- Database Queries

## Runtime Architecture

```text
User
 ↓
Frontend
 ↓
FastAPI
 ↓
Intent Extraction
 ↓
Query Planner
 ↓
SQL Templates
 ↓
PostgreSQL
 ↓
Analytics Engine
 ↓
Report Generator
 ↓
Frontend
```

## Success Criteria

The platform must:

- Answer natural language analytics questions
- Query PostgreSQL
- Generate analyst reports
- Produce charts
- Support millions of records
- Run locally