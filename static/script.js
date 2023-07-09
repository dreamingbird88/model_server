const inferForm = document.querySelector('.infer-form');

const inputText = async (text) => {
    const inferResponse = await fetch(`infer/?input=${text}`);
    const inferJson = await inferResponse.json();

    return inferJson.output;
};

inferForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const textInput = document.getElementById('text-input');
  const inferOutput = document.querySelector('.infer-output');

  try {
    inferOutput.textContent = await inputText(textInput.value);
  } catch (err) {
    console.error(err);
  }
});

const modelForm = document.querySelector('.model-form');
const modelInfo = async (task, name) => {
    const inferResponse = await fetch(`model/?task=${task}&name=${name}`);
    const inferJson = await inferResponse.json();
    return inferJson.output;
};

modelForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const modelTaskInput = document.getElementById('model-task-input');
  const modelNameInput = document.getElementById('model-name-input');
  const modelInfoOutput = document.querySelector('.model-info-output');

  try {
    modelInfoOutput.textContent = await modelInfo(modelTaskInput.value, modelNameInput.value);
  } catch (err) {
    console.error(err);
  }
});
