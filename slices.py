# slices.py

# Common slices used across different traits
common_slices = {
    'RGB': [
        ('RGB', '157', slice(15, 18)),
        ('RGB', '174', slice(21, 24)),
        ('RGB', '190', slice(31, 34)),
        ('RGB', '205', slice(37, 40)),
        ('RGB', '221', slice(43, 46)),
        ('RGB', '231', slice(49, 52)),
        ('RGB', '247', slice(55, 58)),
        ('RGB', '262', slice(61, 64)),
        ('RGB', '279', slice(67, 70)),
        ('RGB', '310', slice(73, 76)),
        ('RGB', '332', slice(79, 82))
    ],
    'RGBRENIR': [
        ('RGBRENIR', '157', slice(15, 20)),
        ('RGBRENIR', '174', slice(21, 26)),
        ('RGBRENIR', '190', slice(31, 36)),
        ('RGBRENIR', '205', slice(37, 42)),
        ('RGBRENIR', '221', slice(43, 48)),
        ('RGBRENIR', '231', slice(49, 54)),
        ('RGBRENIR', '247', slice(55, 60)),
        ('RGBRENIR', '262', slice(61, 66)),
        ('RGBRENIR', '279', slice(67, 72)),
        ('RGBRENIR', '310', slice(73, 78)),
        ('RGBRENIR', '332', slice(79, 84))
    ],
    'CSMRGBRENIR': [
        ('CSMRGBRENIR', '157', slice(14, 20)),
        ('CSMRGBRENIR', '174', slice(20, 26)),
        ('CSMRGBRENIR', '190', slice(30, 36)),
        ('CSMRGBRENIR', '205', slice(36, 42)),
        ('CSMRGBRENIR', '221', slice(42, 48)),
        ('CSMRGBRENIR', '231', slice(48, 54)),
        ('CSMRGBRENIR', '247', slice(54, 60)),
        ('CSMRGBRENIR', '262', slice(60, 66)),
        ('CSMRGBRENIR', '279', slice(66, 72)),
        ('CSMRGBRENIR', '310', slice(72, 78)),
        ('CSMRGBRENIR', '332', slice(78, 84))
    ]
}

# Trait-specific slices
slices = {
    'f50_head_date': {
        'RGB': [
            ('RGB', '205', slice(37, 40)),
            ('RGB', '262', slice(61, 64)),
            ('RGB', '279', slice(67, 70)),
            ('RGB', '332', slice(79, 82))
        ],
        'RGBRENIR': [
            ('RGBRENIR', '205', slice(37, 42)),
            ('RGBRENIR', '262', slice(61, 66)),
            ('RGBRENIR', '279', slice(67, 72)),
            ('RGBRENIR', '332', slice(79, 84))
        ],
        'CSMRGBRENIR': [
            ('CSMRGBRENIR', '205', slice(36, 42)),
            ('CSMRGBRENIR', '262', slice(60, 66)),
            ('CSMRGBRENIR', '279', slice(66, 72)),
            ('CSMRGBRENIR', '332', slice(78, 84))
        ]
    },
    'culm_length': common_slices,
    'biomass': common_slices
}

def get_slices_for_trait(trait):
    """
    Retrieve the slices configuration for a given trait.

    Args:
        trait (str): The trait to get the slices configuration for.

    Returns:
        dict: The configuration of slices for the specified trait.
    """
    return slices.get(trait, {})
