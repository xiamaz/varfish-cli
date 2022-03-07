"""Implementation of ``varfish-cli small-var-query-fetch-results``"""

import argparse
import json
import sys
import uuid

from logzero import logger

from varfish_cli import api
from varfish_cli.case.config import CaseSmallVariantQueryFetchResultsConfig


def setup_argparse(parser):
    parser.add_argument("--hidden-cmd", dest="case_cmd", default=run, help=argparse.SUPPRESS)
    parser.add_argument(
        "query_uuid", help="UUID of the query to fetch results for.", type=uuid.UUID
    )


def run(config, toml_config, args, _parser, _subparser, file=sys.stdout):
    """Run fetch results command."""
    config = CaseSmallVariantQueryFetchResultsConfig.create(args, config, toml_config)
    logger.info("Configuration: %s", config)
    logger.info("Fetching results")
    base_config = config.case_config.global_config
    res = api.small_var_query_fetch_results(
        server_url=base_config.varfish_server_url,
        api_token=base_config.varfish_api_token,
        query_uuid=args.query_uuid,
    )

    print("Query Results", file=file)
    print("=============", file=file)
    print(file=file)
    json.dump(res, file, indent="  ")
