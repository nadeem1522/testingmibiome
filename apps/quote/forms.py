from django import forms


class QuoteForm(forms.Form):
    company_name = forms.CharField(label='Company / University Name')
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    contact = forms.CharField(label='Contact Number')
    email = forms.CharField(label='Email ID')
    project_name = forms.CharField(label='Project Name')
    project_use = forms.ChoiceField(
        label='Planned use(s) of the project',
        choices=(
            ('Basic Research', 'Basic Research'),
            ('Clinical Research', 'Clinical Research'),
            ('Diagnostic', 'Diagnostic')
        )
    )
    study_nature = forms.ChoiceField(
        label='Nature of study',
        choices=(
            ('Longitudinal', 'Longitudinal'),
            ('One time', 'One time')
        )
    )
    start_date = forms.DateField(label='Tentative start date')
    project_objective = forms.CharField(label='Project objective')
    project_outcome = forms.CharField(label='Project outcome expectations')
    service_choice = forms.ChoiceField(
        label='Please mention choice of service',
        choices=(
            ('DNA Sequencing', 'DNA Sequencing'),
            ('RNA Sequencing', 'RNA Sequencing'),
            ('Epigenetics', 'Epigenetics'),
            ('Microarray', 'Microarray'),
            ('10X', '10X'),
            ('Pacbio', 'Pacbio'),
            ('Metagenomics', 'Metagenomics'),
            ('Metatranscriptomics', 'Metatranscriptomics'),
        )
    )
    specific_service = forms.ChoiceField(
        label='Please select specific service',
        choices=(
            ('Whole Genome Sequencing', 'Whole Genome Sequencing'),
            ('Whole Exome Sequencing', 'Whole Exome Sequencing'),
            ('Denovo Sequencing', 'Denovo Sequencing'),
            ('Genotyping-By-Sequencing', 'Genotyping-By-Sequencing'),
            ('Whole Transcriptome analysis', 'Whole Transcriptome analysis'),
            ('Long non-coding RNA', 'Long non-coding RNA'),
            ('Isoform Sequencing', 'Isoform Sequencing'),
            ('MeDIP-Seq', 'MeDIP-Seq'), ('ChIP-Seq', 'ChIP-Seq'),
            ('Whole Genome Bi-sulfite Sequencing','Whole Genome Bi-sulfite Sequencing'),
            ('ATAC-Seq', 'ATAC-Seq'), ('Gene Expression', 'Gene Expression'),
            ('Copy number variation', 'Copy number variation'),
            ('miRNA profiling', 'miRNA profiling'), ('Custom', 'Custom'),
            ('Single Cell Genome Sequencing', 'Single Cell Genome Sequencing'),
            ('Single Cell ATAC Sequencing', 'Single Cell ATAC Sequencing'),
            ('Single Cell RNA Sequencing', 'Single Cell RNA Sequencing'),
            ('Pacbio Genome Sequencing', 'Pacbio Genome Sequencing'),
            ('Pacbio Isoseq Sequencing', 'Pacbio Isoseq Sequencing'),
            ('Shotgun Metagenome', 'Shotgun Metagenome'),
            ('16S/18S rDNA', '16S/18S rDNA'),
            ('ITS sequencing', 'ITS sequencing'),
            ('Enriched for coding RNA', 'Enriched for coding RNA'),
            ('16S rRNA', '16S rRNA'),
        )
    )
    customized_service = forms.CharField(
        label='Customized service (please elaborate nature of service needed)',
        required=False
    )
    ngs_platform = forms.ChoiceField(
        label='Platform',
        choices=(
            ('Illumina (Novaseq6000)', 'Illumina (Novaseq6000)'),
            ('Illumina (MiSeq)', 'Illumina (MiSeq)'),
            ('Nanopore', 'Nanopore'),
            ('Illumina followed by Nanopore', 'Illumina followed by Nanopore'),
            ('Ion Torrent', 'Ion Torrent'),
            ('10X Chromium', '10X Chromium'),
            ('PacBio', 'PacBio'),
            ('Affymetrix', 'Affymetrix'),
            ('Others', 'Others'),
        )
    )
    ngs_specify = forms.CharField(
        label='If NGS PLatform Others, please specify',
        required=False
    )
    model_type = forms.CharField(label='Model type')
    sample_type = forms.ChoiceField(
        label='Sample type',
        choices=(
            ('Genomic DNA', 'Genomic DNA'),
            ('Metagenomic DNA', 'Metagenomic DNA'),
            ('Enriched DNA', 'Enriched DNA'),
            ('Total RNA', 'Total RNA'),
            ('Enriched RNA', 'Enriched RNA'),
            ('PCR products', 'PCR products'),
            ('Tissue Sample', 'Tissue Sample'),
            ('FFPE', 'FFPE'),
            ('Stool', 'Stool'),
            ('Surface swab', 'Surface swab'),
            ('Soil', 'Soil'),
            ('Water', 'Water'),
            ('Others', 'Others'),
        )
    )
    sample_type_specify = forms.CharField(
        label='If sample type Others, please specify',
        required=False
    )
    prepared_library = forms.CharField(
        label='Prepared library (please mention kit used)')
    sample_number = forms.CharField(label='Number of samples')
    sequencing_parameter = forms.ChoiceField(
        label='Sequencing Parameters (read length)',
        choices=(
            ('Single end: 50', 'Single end: 50'),
            ('Paired end: 75', 'Paired end: 75'),
            ('Paired end: 150', 'Paired end: 150'),
            ('Paired end: 250', 'Paired end: 250'),
            ('Paired end: 300', 'Paired end: 300'),
        )
    )
    sequencing_other = forms.CharField(
        label='Any other sequencing parameter',
        required=False
    )
    sequencing_depth = forms.ChoiceField(
        label='Required Sequencing Depth per sample',
        choices=(
            ('30X', '30X'),
            ('50X', '50X'),
            ('100X', '100X'),
        )
    )
    expected_data = forms.ChoiceField(
        label='Expected Data size in Gb per sample',
        choices=(
            ('Upto 2 Gb', 'Upto 2 Gb'),
            ('2-10 Gb', '2-10 Gb'),
            ('10-20 Gb', '10-20 Gb'),
            ('20-100 Gb', '20-100 Gb'),
            ('Others', 'Others'),
        )
    )
    expected_data_specify = forms.CharField(
        label='If expected data Others, please specify',
        required=False
    )
    reference_genome = forms.CharField(
        label='Reference genome name (if available, which will be utilized for post-sequencing analysis) Reference genome size in bp if any',
        required=False
    )
    data_analysis = forms.ChoiceField(
        label='Data analysis activities',
        choices=(
            ('QC of raw reads', 'QC of raw reads'),
            ('Genome assembly: Reference based', 'Genome assembly: Reference based'),
            ('Genome assembly: De novo', 'Genome assembly: De novo'),
            ('Quantifying transcipt abundance', 'Quantifying transcipt abundance'),
            ('DGE analysis', 'DGE analysis'),
            ('Comparative genomics: SNP/in-del', 'Comparative genomics: SNP/in-del'),
            ('Report of analysis', 'Report of analysis'),
            ('Others', 'Others'),
        )
    )
    data_analysis_specify = forms.CharField(
        label='If data analysis activities Others, please specify',
        required=False
    )
    data_delivery = forms.ChoiceField(
        label='Data Delivery method',
        choices=(
            ('HDD', 'HDD'),
            ('Server', 'Server'),
            ('Cloud Storage', 'Cloud Storage'),
        )
    )
    data_stored = forms.ChoiceField(
        label='Data stored with miBiome',
        choices=(
            ('Yes', 'Yes'),
            ('No', 'No'),
        )
    )
    comments = forms.CharField(
        label='Comments',
        required=False
    )
    hear_us = forms.ChoiceField(
        label='For first time customers: How did you hear about us?',
        choices=(
            ('Internet', 'Internet'),
            ('Website', 'Website'),
            ('Contact', 'Contact'),
            ('Others', 'Others'),
        ),
        required=False
    )
    hear_us_specify = forms.CharField(
        label='If How did you hear about us?, Others, please specify',
        required=False
    )


class SampleSubForm(forms.Form):
    company_name = forms.CharField(label='Company / University Name')
    name = forms.CharField(label='Name')
    contact = forms.CharField(label='Contact Number')
    email = forms.CharField(label='Email ID')
    project_name = forms.CharField(label='Project Name')
    invoice_address = forms.CharField(label='Invoice Address')
    data_del_add = forms.CharField(label='Data Delivery Address')
    sample_shipping_date = forms.DateField(label='Sample Shipping Date')
    order_date = forms.DateField(label='Order Date')
    courier_name = forms.CharField(label='Courier Name')
    tracking_details = forms.CharField(label='Tracking Details')
    sample_number = forms.CharField(label='Number of Samples/Library')
    sample_type = forms.ChoiceField(
        label='Sample type',
        choices=(
            ('Genomic DNA', 'Genomic DNA'),
            ('Metagenomic DNA', 'Metagenomic DNA'),
            ('Enriched DNA', 'Enriched DNA'),
            ('Total RNA', 'Total RNA'),
            ('Enriched RNA', 'Enriched RNA'),
            ('PCR products', 'PCR products'),
            ('Tissue Sample', 'Tissue Sample'),
            ('FFPE', 'FFPE'),
            ('Stool', 'Stool'),
            ('Surface swab', 'Surface swab'),
            ('Soil', 'Soil'),
            ('Water', 'Water'),
            ('Others', 'Others'),
        )
    )
    sample_type_specify = forms.CharField(
        label='If sample type Others, please specify',
        required=False
    )
    extraction_method = forms.CharField(label='Mehod of extraction')
    samples_in = forms.ChoiceField(
        label='Samples In',
        choices=(
            ('Dissolved in nuclease free water', 'Dissolved in nuclease free water'),
            ('Dissolved in TE Buffer', 'Dissolved in TE Buffer'),
            ('Dissolved in 10mM Tris-Cl pH 8.0 Buffer', 'Dissolved in 10mM Tris-Cl pH 8.0 Buffer'),
            ('Suspended in Alcohol', 'Suspended in Alcohol'),
            ('Lyophilized', 'Lyophilized'),
            ('Others', 'Others')
        )
    )
    samples_in_specify = forms.CharField(
        label='If samples in Others, please specify',
        required=False
    )
    ngs_platform = forms.ChoiceField(
        label='Platform',
        choices=(
            ('Illumina (Novaseq6000)', 'Illumina (Novaseq6000)'),
            ('Illumina (MiSeq)', 'Illumina (MiSeq)'),
            ('Nanopore', 'Nanopore'),
            ('Illumina followed by Nanopore', 'Illumina followed by Nanopore'),
            ('Ion Torrent', 'Ion Torrent'),
            ('10X Chromium', '10X Chromium'),
            ('PacBio', 'PacBio'),
            ('Affymetrix', 'Affymetrix'),
            ('Others', 'Others'),
        )
    )
    ngs_specify = forms.CharField(
        label='If platform Others, please specify',
        required=False
    )
    sequencing_parameter = forms.ChoiceField(
        label='Sequencing Parameters (read length)',
        choices=(
            ('Single end: 50', 'Single end: 50'),
            ('Paired end: 75', 'Paired end: 75'),
            ('Paired end: 150', 'Paired end: 150'),
            ('Paired end: 250', 'Paired end: 250'),
            ('Paired end: 300', 'Paired end: 300'),
        )
    )
    sequencing_other = forms.CharField(
        label='Any other sequencing parameter',
        required=False
    )
    service_choice = forms.ChoiceField(
        label='Please mention choice of service',
        choices=(
            ('DNA Sequencing', 'DNA Sequencing'),
            ('RNA Sequencing', 'RNA Sequencing'),
            ('Epigenetics', 'Epigenetics'),
            ('Microarray', 'Microarray'),
            ('10X', '10X'),
            ('Pacbio', 'Pacbio'),
            ('Metagenomics', 'Metagenomics'),
            ('Metatranscriptomics', 'Metatranscriptomics'),
        )
    )
    specific_service = forms.ChoiceField(
        label='Please select specific service',
        choices=(
            ('Whole Genome Sequencing', 'Whole Genome Sequencing'),
            ('Whole Exome Sequencing', 'Whole Exome Sequencing'),
            ('Denovo Sequencing', 'Denovo Sequencing'),
            ('Genotyping-By-Sequencing', 'Genotyping-By-Sequencing'),
            ('Whole Transcriptome analysis', 'Whole Transcriptome analysis'),
            ('Long non-coding RNA', 'Long non-coding RNA'),
            ('Isoform Sequencing', 'Isoform Sequencing'),
            ('MeDIP-Seq', 'MeDIP-Seq'), ('ChIP-Seq', 'ChIP-Seq'),
            ('Whole Genome Bi-sulfite Sequencing','Whole Genome Bi-sulfite Sequencing'),
            ('ATAC-Seq', 'ATAC-Seq'), ('Gene Expression', 'Gene Expression'),
            ('Copy number variation', 'Copy number variation'),
            ('miRNA profiling', 'miRNA profiling'), ('Custom', 'Custom'),
            ('Single Cell Genome Sequencing', 'Single Cell Genome Sequencing'),
            ('Single Cell ATAC Sequencing', 'Single Cell ATAC Sequencing'),
            ('Single Cell RNA Sequencing', 'Single Cell RNA Sequencing'),
            ('Pacbio Genome Sequencing', 'Pacbio Genome Sequencing'),
            ('Pacbio Isoseq Sequencing', 'Pacbio Isoseq Sequencing'),
            ('Shotgun Metagenome', 'Shotgun Metagenome'),
            ('16S/18S rDNA', '16S/18S rDNA'),
            ('ITS sequencing', 'ITS sequencing'),
            ('Enriched for coding RNA', 'Enriched for coding RNA'),
            ('16S rRNA', '16S rRNA'),
        )
    )
    sequencing_depth = forms.ChoiceField(
        label='Required Sequencing Depth per sample',
        choices=(
            ('30X', '30X'),
            ('50X', '50X'),
            ('100X', '100X'),
        )
    )
    expected_data = forms.ChoiceField(
        label='Expected Data size in Gb per sample',
        choices=(
            ('Upto 2 Gb', 'Upto 2 Gb'),
            ('2-10 Gb', '2-10 Gb'),
            ('10-20 Gb', '10-20 Gb'),
            ('20-100 Gb', '20-100 Gb'),
            ('Others', 'Others'),
        )
    )
    expected_data_specify = forms.CharField(
        label='If expected data Others, please specify',
        required=False
    )
    bioinfo_standard = forms.CharField(
        label='Bioinformatics Analysis (Standard)',
        required=False
    )
    bioinfo_additional = forms.CharField(
        label='Bioinformatics Analysis (Additional)',
        required=False
    )
    reference_genome = forms.CharField(
        label='Reference genome name (if available, which will be utilized for post-sequencing analysis) Reference genome size in bp if any',
        required=False
    )
    data_delivery = forms.ChoiceField(
        label='Data Delivery method',
        choices=(
            ('HDD', 'HDD'),
            ('Server', 'Server'),
            ('Cloud Storage', 'Cloud Storage'),
            ('Data stored with miBiome', 'Data stored with miBiome'),
        )
    )
    transportation = forms.ChoiceField(
        label='Transportation Details',
        choices=(
            ('Dry Ice', 'Dry Ice'),
            ('Cool Pack', 'Cool Pack'),
            ('Room Temperature', 'Room Temperature'),
        )
    )
    comments = forms.CharField(
        label='Comments',
        required=False
    )