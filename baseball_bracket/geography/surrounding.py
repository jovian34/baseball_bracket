surrounding_map = {
    'FL': ('AL', 'GA'),
    'GA': ('TN', 'NC', 'SC', 'FL', 'AL'),
    'SC': ('GA', 'NC'),
    'NC': ('VA', 'TN', 'SC'),
    'VA': ('NC', 'WV', 'MD', 'DE', 'PA'),
    'MD': ('VA', 'WV', 'DE', 'PA', 'NJ'),
    'DE': ('VA', 'MD', 'PA', 'NJ'),
    'NJ': ('PA', 'NY', 'CT', 'RI'),
    'CT': ('NJ', 'NY', 'VT', 'NH', 'ME', 'MA', 'RI'),
    'RI': ('NJ', 'NY', 'VT', 'NH', 'ME', 'MA', 'CT'),
    'MA': ('NJ', 'NY', 'VT', 'NH', 'ME', 'RI', 'CT'),
    'ME': ('NJ', 'NY', 'VT', 'NH', 'RI', 'MA', 'CT'),
    'NH': ('NJ', 'NY', 'VT', 'RI', 'ME', 'MA', 'CT'),
    'VT': ('NJ', 'NY', 'RI', 'NH', 'ME', 'MA', 'CT'),
    'NY': ('NJ', 'RI', 'VT', 'NH', 'ME', 'MA', 'CT', 'PA'),
    'PA': ('NY', 'NJ', 'DE', 'MD', 'VA', 'WV', 'OH'),
    'WV': ('OH', 'PA', 'MD', 'VA', 'KY'),
    'OH': ('MI', 'IN', 'PA', 'WV', 'KY'),
    'MI': ('WI', 'IN', 'OH'),
    'IN': ('MI', 'OH', 'KY', 'IL'),
    'KY': ('IN', 'OH', 'WV', 'VA', 'TN', 'MO'),
    'TN': ('MO', 'KY', 'VA', 'NC', 'GA', 'AL', 'MS', 'AR'),
    'AL': ('TN', 'GA', 'FL', 'MS'),
    'MS': ('LA', 'AR', 'TN', 'AL'),
    'LA': ('TX', 'AR', 'MS'),
    'AR': ('LA', 'TX', 'OK', 'MO', 'TN', 'MS'),
    'WI': ('IL', 'IA', 'MN', 'MI'),
    'IL': ('WI', 'IN', 'KY', 'MO', 'IA'),
    'MN': ('ND', 'SD', 'WI', 'IL', 'IA'),
    'IA': ('MO', 'NE', 'SD', 'MN', 'WI', 'IL'),
    'MO': ('IA', 'IL', 'KY', 'TN', 'AR', 'OK', 'KS', 'NE'),
    'ND': ('SD', 'MT', 'MN'),
    'SD': ('WY', 'MT', 'ND', 'MN', 'IA', 'NE'),
    'AK': (),
    'HI': (),
    'NE': ('WY', 'SD', 'IA', 'MO', 'KS', 'CO'),
    'KS': ('OK', 'CO', 'NE', 'MO'),
    'OK': ('KS', 'MO', 'AR', 'TX', 'NM', 'CO'),
    'TX': ('NM', 'OK', 'AR', 'LA'),
    'MT': ('ID', 'WY', 'ND', 'SD'),
    'WY': ('UT', 'ID', 'MT', 'SD', 'NE', 'CO'),
    'CO': ('NE', 'KS', 'OK', 'NM', 'UT', 'WY'),
    'NM': ('AZ', 'UT', 'CO', 'OK', 'TX'),
    'ID': ('NV', 'OR', 'MT', 'UT', 'WY', 'WA'),
    'UT': ('AZ', 'NV', 'ID', 'WY', 'CO', 'NM'),
    'AZ': ('CA', 'NV', 'NM', 'UT'),
    'NV': ('CA', 'OR', 'ID', 'UT', 'AZ'),
    'WA': ('ID', 'OR'),
    'OR': ('WA', 'CA', 'ID', 'NV'),
    'CA': ('OR', 'NV', 'AZ')
}
