def get_model_prediction(image, prompt):
    try:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Replace with the correct model URL
        model_prediction = Model(
            "https://clarifai.com/openai/chat-completion/models/gpt-4-vision"
        ).predict_by_bytes(
            prompt.encode(),
            input_type="text",
            inference_params={
                "temperature": 0.2,
                "image_base64": base64_image,
            },
        )
        return model_prediction.outputs[0].data.text.raw
    except Exception as e:
        print(f"Error in get_model_prediction function: {e}")
        return "Error getting prediction"
