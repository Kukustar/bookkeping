const ApiService = {
  /**
   *
   * @param url
   * @param query
   * @param router
   * @returns {Promise<void>}
   */
  async get (url, query, router) {
    const token = localStorage.getItem('access')
    const options = {
      method: 'GET',
      mode: 'cors',
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
    try {
      // eslint-disable-next-line
      const res = await fetch(`${url}`, options)
      const { status, statusText } = res
      if (status === 401 && statusText === 'Unauthorized') {
        localStorage.removeItem('access')
        localStorage.removeItem('expireDate')
        localStorage.removeItem('refresh')
        router.push('/login')
      }
      return await res.json()
    } catch (e) {
      console.info(e)
    }
  },
  async post (url, data, router) {
    const token = localStorage.getItem('access')
    const options = {
      method: 'POST',
      mode: 'cors',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }

    try {
      const res = await fetch(`${url}`, options)
      const { status, statusText } = res
      if (status === 401 && statusText === 'Unauthorized') {
        localStorage.removeItem('access')
        localStorage.removeItem('expireDate')
        localStorage.removeItem('refresh')
        router.push('/login')
      }
      return await res.json()
    } catch (e) {
      console.info(e)
    }
  },
  async delete (url, id, router) {
    const token = localStorage.getItem('access')
    const options = {
      method: 'delete',
      mode: 'cors',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    }

    try {
      const res = await fetch(`${url}${id}/`, options)
      const { status, statusText } = res
      if (status === 401 && statusText === 'Unauthorized') {
        localStorage.removeItem('access')
        localStorage.removeItem('expireDate')
        localStorage.removeItem('refresh')
        router.push('/login')
      }
      return await res.json()
    } catch (e) {
      console.info(e)
    }
  }
}

export default ApiService
