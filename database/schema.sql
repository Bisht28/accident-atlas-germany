DROP TABLE IF EXISTS indicator_values CASCADE;
DROP TABLE IF EXISTS indicators CASCADE;
DROP TABLE IF EXISTS accidents CASCADE;
DROP TABLE IF EXISTS regions CASCADE;
DROP TABLE IF EXISTS etl_runs CASCADE;

CREATE TABLE regions (
    region_id BIGSERIAL PRIMARY KEY,

    state_code VARCHAR(10),
    state_name VARCHAR(255),

    district_code VARCHAR(20),
    district_name VARCHAR(255),

    municipality_code VARCHAR(20),
    municipality_name VARCHAR(255),

    region_type VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accidents (
    accident_id BIGSERIAL PRIMARY KEY,

    source_year INTEGER NOT NULL,

    accident_year INTEGER,
    accident_month INTEGER,
    accident_hour INTEGER,
    accident_weekday INTEGER,

    state_code VARCHAR(10),
    district_code VARCHAR(20),
    municipality_code VARCHAR(20),

    severity_category INTEGER,
    accident_type INTEGER,
    accident_subtype INTEGER,

    is_bicycle BOOLEAN DEFAULT FALSE,
    is_pedestrian BOOLEAN DEFAULT FALSE,
    is_car BOOLEAN DEFAULT FALSE,
    is_motorcycle BOOLEAN DEFAULT FALSE,
    is_goods_vehicle BOOLEAN DEFAULT FALSE,
    is_other_vehicle BOOLEAN DEFAULT FALSE,

    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE indicators (
    indicator_id BIGSERIAL PRIMARY KEY,

    indicator_code VARCHAR(100) UNIQUE NOT NULL,
    indicator_name VARCHAR(255) NOT NULL,
    indicator_description TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE indicator_values (
    value_id BIGSERIAL PRIMARY KEY,

    indicator_id BIGINT NOT NULL REFERENCES indicators(indicator_id),

    region_id BIGINT REFERENCES regions(region_id),

    year INTEGER NOT NULL,

    value NUMERIC(20,4),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE etl_runs (
    run_id BIGSERIAL PRIMARY KEY,

    job_name VARCHAR(255) NOT NULL,

    status VARCHAR(50) NOT NULL,

    records_processed BIGINT DEFAULT 0,

    started_at TIMESTAMP,

    completed_at TIMESTAMP,

    message TEXT
);

CREATE INDEX idx_accidents_year
ON accidents(accident_year);

CREATE INDEX idx_accidents_state
ON accidents(state_code);

CREATE INDEX idx_accidents_district
ON accidents(district_code);

CREATE INDEX idx_accidents_municipality
ON accidents(municipality_code);

CREATE INDEX idx_accidents_bicycle
ON accidents(is_bicycle);

CREATE INDEX idx_accidents_pedestrian
ON accidents(is_pedestrian);

CREATE INDEX idx_accidents_car
ON accidents(is_car);

CREATE INDEX idx_accidents_motorcycle
ON accidents(is_motorcycle);

CREATE INDEX idx_indicator_values_year
ON indicator_values(year);

CREATE INDEX idx_indicator_values_region
ON indicator_values(region_id);

CREATE INDEX idx_regions_state
ON regions(state_name);

CREATE INDEX idx_regions_district
ON regions(district_name);

CREATE INDEX idx_regions_municipality
ON regions(municipality_name);