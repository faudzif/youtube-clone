CREATE TABLE vidoes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    tags TEXT[],
    s3_key TEXT NOT NULL,   -- e.g. "videos/my-video.mp4"
    thumbnail_s3_key TEXT,
    duration INT,
    views INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT now()    
);