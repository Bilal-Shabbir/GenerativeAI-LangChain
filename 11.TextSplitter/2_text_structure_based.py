from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Project Mercury Report - Q3 2024
Section 1: Initial Findings The core objective of Project Mercury was achieved with 98% efficiency. The deployment phase experienced zero critical failures, validating the initial hypothesis regarding network optimization. Key performance indicators (KPIs) related to latency saw a 15% improvement month-over-month. This initial success sets the stage for scaling the infrastructure to handle the projected load increase for the upcoming holiday season. The team utilized internal documentation extensively, ensuring compliance with all existing security protocols.

Section 2: Component Breakdown The infrastructure relies heavily on three primary components: the Redis cache cluster, the primary PostgreSQL database, and the external API gateway. The Redis cluster operates at 99.99% uptime, serving as the immediate bottleneck for further speed increases. The database schema remains stable, requiring no major migrations in the current quarter. Monitoring established that the external API gateway is the single point of failure and requires immediate architectural review to introduce redundancy and improve resilience.

Section 3: Future Recommendations Based on Q3 data, the primary recommendation is to refactor the external API gateway for fault tolerance. Secondary recommendations include migrating the primary database cluster to a newer version to leverage enhanced indexing capabilities, which should further reduce query latency by an estimated 5%. We propose a three-week discovery phase in October to scope the migration process. No immediate staffing changes are required for Q4, though specialized expertise may be necessary for the database migration phase."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size =300, 
    chunk_overlap = 0
)
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)