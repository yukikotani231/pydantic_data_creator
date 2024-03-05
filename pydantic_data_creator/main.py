import argparse
import os
import sys
from importlib import import_module
from pydantic import BaseModel
from dataclasses import is_dataclass

import streamlit as st
import streamlit_pydantic as sp


sys.path.append(os.getcwd())


def main(module_path: str, model_name: str):
    module = import_module(module_path)
    model = getattr(module, model_name)

    if not issubclass(model, BaseModel) and not is_dataclass(model):
        st.error(f"{module_path}.{model_name} is not a valid pydantic model or dataclass.")
        st.stop()

    data = sp.pydantic_form(key="my_form", model=model)
    if data:
        st.download_button(
            label="Download JSON",
            data=data.json(indent=2, ensure_ascii=False),
            file_name=f"{model_name}.json",
            mime="application/json",
        )
        st.json(data.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module_path", help="The path to the module that includes the pydantic models"
    )
    parser.add_argument("model_name", help="The name of the pydantic model to use for the form")
    args = parser.parse_args()

    main(args.module_path, args.model_name)
