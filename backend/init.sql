CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS videos (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  title         TEXT        NOT NULL,
  description   TEXT,
  category      TEXT,
  tags          TEXT[],
  s3_key        TEXT        NOT NULL,
  thumbnail_url TEXT,
  duration      INT,
  views         INT         DEFAULT 0,
  created_at    TIMESTAMP   DEFAULT now()
);

-- seed a few rows so the frontend has something to show immediately
INSERT INTO videos (title, description, category, tags, s3_key, thumbnail_url, duration)
VALUES
  ('Python FastAPI Crash Course', 'Learn FastAPI from scratch', 'Education', ARRAY['python', 'fastapi', 'backend'], 'videos/fastapi-crash-course.mp4', 'https://picsum.photos/seed/1/320/180', 3600),
  ('Next.js 14 Full Tutorial',    'App Router deep dive',       'Education', ARRAY['nextjs', 'react', 'frontend'],  'videos/nextjs-tutorial.mp4',        'https://picsum.photos/seed/2/320/180', 5400),
  ('Docker for Developers',       'Containers explained simply','DevOps',    ARRAY['docker', 'devops'],              'videos/docker-for-devs.mp4',         'https://picsum.photos/seed/3/320/180', 2700);