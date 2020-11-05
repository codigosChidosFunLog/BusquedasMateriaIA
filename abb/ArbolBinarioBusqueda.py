from abb.NodoArbol import NodoArbol


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano+1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        self.agregar(c, v)

    def obtener(self, clave, metodo):
        if self.raiz:
            if metodo == 0:
                res = self._obtener(clave, self.raiz)
            elif metodo == 1:
                res = self._buscarPrimeroProfundidad(clave, self.raiz)
            elif metodo == 2:
                res = self._buscarPrimeroAnchura(clave, self.raiz)

            if res:
                return res.cargaUtil
            else:
                return "No existe el dato en el arbol"
        else:
            return "No existe el Arbol"

    def _obtener(self, clave, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def _buscarPrimeroProfundidad(self, clave, nodoActual):
        #print("pasada")
        #print(nodoActual.clave)
        if nodoActual.clave == clave:
            return nodoActual
        if nodoActual.tieneHijoIzquierdo():
            nodo = self._buscarPrimeroProfundidad(clave, nodoActual.hijoIzquierdo)
            if nodo:
                return nodo
        if nodoActual.tieneHijoDerecho():
            nodo = self._buscarPrimeroProfundidad(clave, nodoActual.hijoDerecho)
            if nodo:
                return nodo
        return None

    def _buscarPrimeroAnchura(self, clave, nodoActual):
        #print("pasada")
        #print(nodoActual.clave)
        if nodoActual.clave == clave:
            return nodoActual
        elif nodoActual.tieneHijoIzquierdo() and nodoActual.hijoIzquierdo.clave == clave:
            return nodoActual.hijoIzquierdo
        elif nodoActual.tieneHijoDerecho() and nodoActual.hijoDerecho.clave == clave:
            return nodoActual.hijoDerecho
        if nodoActual.tieneHijoIzquierdo():
            nodo = self._buscarPrimeroAnchura(clave, nodoActual.hijoIzquierdo)
            if nodo:
                return nodo
        if nodoActual.tieneHijoDerecho():
            nodo = self._buscarPrimeroAnchura(clave, nodoActual.hijoDerecho)
            if nodo:
                return nodo
        return None

#0-ObtenerPorClaveNormal
#1-PrimeroProfundidad
#2-PrimeroAnchura
    def __getitem__(self, clave):
        c, metodo = clave
        return self.obtener(c, metodo)
