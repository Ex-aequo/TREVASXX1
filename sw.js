// Service worker do painel TREVASXXI — cache offline de um único ficheiro estático.
// Sem chamadas de rede próprias: o painel não depende de nenhuma API externa.
const CACHE_NAME = 'trevasxxi-v22';
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Cache-first: funciona offline assim que a primeira visita tiver corrido.
// Se atualizares o index.html no GitHub, sobe também a versão do CACHE_NAME (ex.: 'trevasxxi-v2')
// para forçar os browsers a irem buscar a versão nova em vez de servirem a antiga da cache.
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
