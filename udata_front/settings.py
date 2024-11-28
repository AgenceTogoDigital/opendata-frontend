"""
Default settings for udata-front
"""

# TODO: move this back to an extension
RESOURCES_SCHEMAGOUVFR_ENABLED = True
SCHEMA_GOUVFR_VALIDATA_URL = 'https://validata.etalab.studio'
SCHEMA_DOCUMENTATION_URL = 'https://schema.opendata.gouv.tg /'
SCHEMA_PUBLISHING_URL = 'https://publier.etalab.studio/fr'

# Dataset settings
# Default page size for resources on dataset page
RESOURCES_DEFAULT_PAGE_SIZE = 6

# Number of resources to show resource search on dataset page
RESOURCES_MIN_COUNT_TO_SHOW_SEARCH = 12

# Frontend banner parameters
BANNER_ACTIVATED = False
BANNER_HTML_CONTENT_EN = ''
BANNER_HTML_CONTENT_FR = ''

# Demo
DEMO_SERVER_URL = 'https://demo.opendata.gouv.tg '
DEMO_SERVER_NAME = 'demo.opendata.gouv.tg '

# Frontend forms url
DATA_SEARCH_FEEDBACK_FORM_URL = ''
DISCOVERABILITY_FORM_URL = ''
FEEDBACK_FORM_URL = ''
PUBLISHING_FORM_FEEDBACK_URL = ''

# Static pages from github repo
PAGES_GH_REPO_NAME = 'etalab/datagouvfr-pages'
PAGES_REPO_BRANCH = 'master'

# api.gouv.fr
APIGOUVFR_URL = 'https://api.gouv.fr/api/v1/apis'
APIGOUVFR_ALLOW_OPENNESS = ['open', 'semi_open']

# catalogue.opendata.gouv.tg 
CATALOG_URL = 'https://catalogue.opendata.gouv.tg /'

# suport.opendata.gouv.tg 
SUPPORT_URL = 'https://support.opendata.gouv.tg /'

# Guides
GUIDES_URL = 'https://guides.opendata.gouv.tg /'
GUIDES_USER_ACCOUNT_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-opendata.gouv.tg /creer-un-compte-utilisateur-et-rejoindre-une-organisation' # noqa
GUIDES_ORGANIZATION_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-opendata.gouv.tg /organisation/creer-une-organisation' # noqa
GUIDES_DATASET_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-opendata.gouv.tg /jeux-de-donnees/publier-un-jeu-de-donnees' # noqa
GUIDES_REUSE_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-opendata.gouv.tg /reutilisations' # noqa
GUIDES_COMMUNITY_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-opendata.gouv.tg /ressource-communautaire' # noqa
GUIDES_QUALITY_URL = 'https://guides.opendata.gouv.tg /publier-des-donnees/guide-qualite/ameliorer-la-qualite-dun-jeu-de-donnees-en-continu/ameliorer-le-score-de-qualite-des-metadonnees' # noqa

# CAPTCHEtat

# You can activate CaptchEtat, a captcha.com integration by providing
# CAPTCHETAT_BASE_URL, CAPTCHETAT_OAUTH_BASE_URL, CAPTCHETAT_CLIENT_ID and CAPTCHETAT_CLIENT_SECRET
CAPTCHETAT_BASE_URL = None
CAPTCHETAT_OAUTH_BASE_URL = None
CAPTCHETAT_CLIENT_ID = None
CAPTCHETAT_CLIENT_SECRET = None
CAPTCHETAT_TOKEN_CACHE_KEY = 'captchetat-bearer-token'

# ProConnect

# You can activate ProConnect SSO, a https://proconnect.gouv.fr/ login integration
PROCONNECT_OPENID_CONF_URL = None
PROCONNECT_SCOPE = None
PROCONNECT_CLIENT_ID = None
PROCONNECT_CLIENT_SECRET = None

# Newsletter
NEWSLETTER_SUBSCRIPTION_URL = 'https://f.info.opendata.gouv.tg /f/lp/infolettre-data-gouv-fr-landing-page/lk3q01y6'  # noqa

# Metrics API
METRICS_API = None

# recherche-entreprises.api.gouv.fr
SEARCH_SIREN_URL = None

# Metadata quality is hidden for datasets harvested from these backends
QUALITY_METADATA_BACKEND_IGNORE = []
