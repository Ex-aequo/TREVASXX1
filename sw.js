// Service worker do painel TREVASXXI — cache offline de ficheiros estáticos.
// Sem chamadas de rede próprias: o painel não depende de nenhuma API externa.
const CACHE_NAME = 'trevasxxi-v31';
const ASSETS = ['./', './index.html', './manual_pt.json', './mapa3d.html', './manifest.json', './icon-192.png', './icon-512.png'];

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
// Os escudos da vista 3D (images/shields/, ~170 ficheiros, 5 MB no total) NÃO são pré-guardados:
// guardam-se à medida que a vista 3D os pede, e só os dos reinos do teu mapa.
// Se atualizares ficheiros no GitHub, sobe também a versão do CACHE_NAME para forçar os browsers a irem buscar a versão nova.
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((resp) => {
        if (resp && resp.ok && /\/images\/shields\//.test(event.request.url)) {
          const copy = resp.clone();
          caches.open(CACHE_NAME).then((c) => c.put(event.request, copy));
        }
        return resp;
      });
    })
  );
});
