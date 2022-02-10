from cosmotech_scenario_download.generate_main import generate_main


def apply_update(content: dict, scenario_data: dict) -> dict:
    updated_content = content
    # Apply any transformation on the content here
    return updated_content


main = generate_main(apply_update=apply_update)
