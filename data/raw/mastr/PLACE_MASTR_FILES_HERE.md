# Place MaStR Files Here

This directory is intentionally left empty and is not included in the repository.

To execute the full pipeline (`run_full_pipeline.py`), download the German Market Master Data Register (MaStR) XML export and place the source files in the following structure:

```text
data/raw/mastr/
├── marktakteure/
│   └── Marktakteure_*.xml
└── einheiten/
    ├── EinheitenBiomasse.xml
    ├── EinheitenWasser.xml
    ├── EinheitenWind.xml
    └── solar/
        └── EinheitenSolar_*.xml
```

The MaStR export is not included in this repository due to its size (approximately 22 GB uncompressed) and must be obtained separately.

The notebooks expect the folder structure shown above.