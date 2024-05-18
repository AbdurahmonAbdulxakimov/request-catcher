from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        "shop",
        "domain.urls",
        name="domain",
    ),
)
