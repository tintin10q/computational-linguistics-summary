# Interpretability 
When something is interpretable you can know what a certain value or vector of values represent. So with [Connotations](../Semantic-Similarity/Connotations.md) it is clear what each number in the vector means while with the hidden layers of a [neural networks](Feed%20forward%20neural%20networks%20(FFNN).md) it is not clear how exactly the numbers relate to the input. 

This topic is what the guest lecture was about. How do you explain good performance of models. 

Interpretability to prevent scenarios where the model takes a shortcut trough the data and therefor becomes less generalizable. 

## Explaining predictions
Interpretability allows you to explain the predictions of a model. For instance with a linear classifier you can know exactly **why** something was predicted. This is not the case with neural networks but there are approaches to do this. 

### Occlusion 
Occlusion-based methods compute input saliency by occluding (or erasing) input features and measuring how that affects the model output. So deleting parts of the input data and then looking how the model behaves. 

![Occlusion](../images/Pasted%20image%2020220605012313.png)

This can indicate the words for instance a model is picking up on to give a good probability to an answer. 

Occlusions will try taking out every combination of the input which takes a lot of time. 

### Perturbations
With perturbations you basically sample masks which you use to take out some of the input data and you run the model. Then you try to predict these outputs with a linear model from the masks. This linear model will then assign importance scores to some of the words. So you use the fact that linear models are interpretable to interpret your model. 

## Gradient $L_2$
Also known as Sensitivity Analysis (SA), we can use the gradient from a standard backpropagation pass as relevance scores:

In practice, we want a single scalar relevance score  per input word, instead of one for each word embedding dimension, so we take the L2 norm:  Requires one forward pass and one backward pass.

Gradient L2 says how much a change in a word's  embedding affects the output of a model.

Instead of using the gradient to improve the model you use it to explain the results.

Grad L2 shows the sensitivity of the model, i.e., how  much a change in input changes the output.  

## Gradient x Input
You can also take the gradients and multiply them with the embedded inputs. This arrives at the gradients times input measure. To get a scaler you do the dot product between the embedded input and the gradient times. 

Gradient ⨉ Input shows the saliency, i.e., the marginal effect of each input word on the prediction

## Integrated Gradients

Integrated gradients (IG) is a gradient-based method  which deals with the problem of saturation: gradients  may get close to zero for a well-fitted function.  

IG requires a baseline $b_{1:n}$e .g., all-zeros vectors or repeated [MASK] vectors. The math looks like this: $$\frac{1}{m}\sum\limits^{m}_{k=1} \nabla f_c(b_{1:n}+\frac{k}{m}(\mathbf{x}_{1:n}) \cdot (\mathbf{x}_i-b))$$
where m is the number of steps we take (i.e., the  number of gradients we get).


## Layer-wise Relevance Propagation (LRP)
LRP starts with a forward pass to obtain the output  $f_c(x_{1:n})$, which is the top-level relevance.  

It then uses a special backward pass that, at each  layer, redistributes the incoming relevance among  the inputs of that layer.  Each type of layer has its own propagation rules.   E.g. different rules for feed-forward layers and LSTMs.  Relevance is redistributed until we arrive at the input.

For models with only ReLU and max pool nonlinearities, and ε=0, this is the same as Grad*input!

## Attention 
Many models have attention mechanisms. These provide some sense of interpretability. If you visualize them, they show what  the model is "looking at" at one  particular layer.  

- Many papers were written on whether attention is explanation (or not) see [Transformers](Transformers.md)
- A major issue is that, when attention is applied  over hidden states, information from other time steps was already mixed in.  
- It's better to use saliency methods if you want  input importance scores as a model developer.


## New metrix

![](../images/Pasted%20image%2020220605014258.png)

## Language interpretability tool (LIT)

The guest lecturer worked on a tool to interpret models better. 
![Interpreting models](../images/Pasted%20image%2020220605013925.png)

# Towards effective explanations  
- Be careful about describing internal AI representations in human terms (concepts,  
rationalizations) as it communicates intentionality.  
- Be careful about attributing real causes to model reasoning.  
- Allow for interactive explanations to resolve contradictions.  
- Be clear on who the explainees are, what priors they may leverage.