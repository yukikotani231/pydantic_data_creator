import argparse
from importlib import import_module
from pydantic import BaseModel
from dataclasses import is_dataclass

import streamlit as st
import streamlit_pydantic as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module_path", help="The path to the module that includes the pydantic models"
    )
    parser.add_argument("model_name", help="The name of the pydantic model to use for the form")
    args = parser.parse_args()

    module = import_module(args.module_path)
    model = getattr(module, args.model_name)

    if not issubclass(model, BaseModel) and not is_dataclass(model):
        st.error(
            f"{args.module_path}.{args.model_name} is not a valid pydantic model or dataclass."
        )
        st.stop()

    data = sp.pydantic_form(key="my_form", model=model)
    if data:
        st.json(data.json())


if __name__ == "__main__":
    main()