// I got this service worker from https://gist.github.com/JMPerez/8ca8d5ffcc0cc45a8b4e1c279efd8a94

// the cache version gets updated every time there is a new deployment
const CACHE_VERSION = 16;
const CURRENT_CACHE = `main-${CACHE_VERSION}`;

// these are the routes we are going to cache for offline support
const cacheFiles = ['/', 
"/Classification.html",
"/Languages.html",
"/Languages/Zipfian%20Distribution.html",
"/images/Pasted%20image%2020220314185901.webp",
"/Data/Words.html",
"/Languages/Grammar.html",
"/images/Pasted%20image%2020220216154345.webp",
"/Data.html",
"/Prediction/Decoding.html",
"/Classification/Native%20baiyes.html",
"/Prediction/Questions.html",
"/images/Pasted%20image%2020220216120004.webp",
"/images/Pasted%20image%2020211127142855.webp",
"/images/Pasted%20image%2020220217165328.webp",
"/images/tikkies.webp",
"/images/Pasted%20image%2020220215090607.webp",
"/Data/Levels%20of%20analysis.html",
"/images/Pasted%20image%2020220224133421.webp",
"/Languages/CKY.html",
"/images/Pasted%20image%2020220216115427.webp",
"/Data/Treebank.html",
"/Languages/Constituency.html",
"/images/Pasted%20image%2020211127131955.webp",
"/images/Pasted%20image%2020211212165450.webp",
"/Data/Type.html",
"/images/Pasted%20image%2020211212165625.webp",
"/Languages/Alphabeth.html",
"/Data/Normalization.html",
"/images/Pasted%20image%2020211127142739.webp",
"/images/Pasted%20image%2020220308194114.webp",
"/Other/Learning.html",
"/Prediction/Viterbi%20Algorithm.html",
"/Prediction/markov%20assumption.html",
"/index.html",
"/Languages/N-grams.html",
"/network.webp",
"/Prediction/perplexity.html",
"/images/Pasted%20image%2020220216114812.webp",
"/Prediction/Language%20Modeling.html",
"/Classification/Classification.html",
"/Prediction/Overfitting.html",
"/images/Pasted%20image%2020220213185844.png",
"/images/Pasted%20image%2020220314190559.webp",
"/Languages/Ambiguity.html",
"/Prediction/Hidden%20Markov%20Models.html",
"/images/Pasted%20image%2020211127130856.webp",
"/Languages/parsing.html",
"/images/Pasted%20image%2020211127140252.webp",
"/Data/Sentences.html",
"/Data/index.html",
"/images/Pasted%20image%2020220224152619.webp",
"/images/Pasted%20image%2020220216115205.webp",
"/Prediction/OOV%20rate.html",
"/images/Pasted%20image%2020220215090454.png",
"/Languages/Parts%20of%20Speech.html",
"/README.html",
"/Classification/Evaluating%20Classification%20models.html",
"/Data/Lexicon.html",
"/Languages/Languages.html",
"/Languages/Edit%20distance.html",
"/Languages/parsetree.html",
"/images/Pasted%20image%2020220217170600.webp",
"/Other/Things%20that%20he%20said%20come%20at%20the%20exam.html",
"/Classification/Native%20baiyes/Bayes%20rule.html",
"/images/Pasted%20image%2020211212165403.webp",
"/Data/Token.html",
"/images/Pasted%20image%2020220217171236.webp",
"/Classification/Native%20baiyes/Naive%20Bayes%20Classifier.html",
"/images/Pasted%20image%2020220308195301.webp",
"/images/Pasted%20image%2020211127131455.webp",
"/Languages/Context%20free%20grammars.html",
"/images/Pasted%20image%2020211127131012.webp",
"/images/Pasted%20image%2020220223185953.webp",
"/Data/Morphemes.html",
"/images/Pasted%20image%2020211212165811.webp",
"/Data/Symbol.html",
"/Data/Thesaurus.html",
"/images/Pasted%20image%2020211212163706.webp",
"/Classification/contingency%20table.html",
"/images/Pasted%20image%2020220314195726.webp",
"/Languages/chompsky%20heirarchy.html",
"/images/Pasted%20image%2020220216114704.webp",
"/Prediction/Smoothing.html",
"/Languages/Regular%20expression.html",
"/images/Pasted%20image%2020220224152946.webp",
"/images/Pasted%20image%2020220217165311.webp",
"/images/Pasted%20image%2020220216130019.webp",
"/Languages/finite%20state%20automata.html",
"/Prediction/Prediction.html",
"/Languages/Chomsky%20Normal%20Form.html",
"/images/Pasted%20image%2020211127132201.webp",
"/Languages/regular%20languages.html",
"/Other.html",
"/Data/Lemma.html",
"/Other/Goals.html",
"/images/Pasted%20image%2020220215090517.webp",
"/Data/data.html",
"/images/Pasted%20image%2020220314184733.webp",
"/Prediction/Markov%20models.html",
"/Prediction.html",
"/images/Pasted%20image%2020211127132647.webp",
"/Data/Corpus.html",
"/images/Pasted%20image%2020220224154616.webp",
"/Languages/Natural%20languages.html"
];

// on activation we clean up the previously registered service workers
self.addEventListener('activate', evt =>
  evt.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CURRENT_CACHE) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  )
);

// on install we download the routes we want to cache for offline
self.addEventListener('install', evt =>
  evt.waitUntil(
    caches.open(CURRENT_CACHE).then(cache => {
      return cache.addAll(cacheFiles);
    })
  )
);

// fetch the resource from the network
const fromNetwork = (request, timeout) =>
  new Promise((fulfill, reject) => {
    const timeoutId = setTimeout(reject, timeout);
    fetch(request).then(response => {
      clearTimeout(timeoutId);
      fulfill(response);
      update(request);
    }, reject);
  });

// fetch the resource from the browser cache
const fromCache = request =>
  caches
    .open(CURRENT_CACHE)
    .then(cache =>
      cache
        .match(request)
        .then(matching => matching || cache.match('/offline/'))
    );

// cache the current page to make it available for offline
const update = request =>
  caches
    .open(CURRENT_CACHE)
    .then(cache =>
      fetch(request).then(response => cache.put(request, response))
    );

// general strategy when making a request (eg if online try to fetch it
// from the network with a timeout, if something fails serve from cache)
self.addEventListener('fetch', evt => {
  evt.respondWith(
    fromNetwork(evt.request, 10000).catch(() => fromCache(evt.request))
  );
  evt.waitUntil(update(evt.request));
});
