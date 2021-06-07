/**
 *
 * @param to -  path to route
 * @param from - path from route
 * @param next - function call next route
 */
export default function jwtGuard (to, from, next) {
  const accessToken = localStorage.getItem('access')
  const refreshToken = localStorage.getItem('refresh')
  const unixExpireDate = localStorage.getItem('expireDate')
  const unixExpireRefreshDate = localStorage.getItem('expireRefreshTokenExpireDate')
  const expireRefreshTokenDate = new Date(parseInt(unixExpireRefreshDate))
  const expireDate = new Date(parseInt(unixExpireDate))
  const nowDate = new Date()
  const dateDiff = expireDate - nowDate
  const dateRefreshTokenDiff = expireRefreshTokenDate - nowDate

  if (to.name !== 'Login' && (accessToken === null || accessToken === undefined)) next({ name: 'Login' })
  if (to.name !== 'Login' && (refreshToken === null || refreshToken === undefined)) next({ name: 'Login' })
  if (to.name !== 'Login' && dateDiff < 0 && dateRefreshTokenDiff > 0) {
    fetch('http://localhost:3003/api/token/refresh/', {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        refresh: refreshToken
      })
    })
      .then(result => result.json())
      .then(reset => {
        const { access } = reset
        if (typeof access === 'string') {
          const nowDate = new Date()
          const expireDate = new Date(nowDate.getTime() + 5 * 60000)
          const unixExpireDate = +new Date(expireDate)
          localStorage.setItem('access', access)
          localStorage.setItem('expireDate', String(unixExpireDate))

          next()
        } else next({ name: 'Login' })
      })
      .catch(e => {
        console.info(e)
        next({ name: 'Login' })
      })
  } else next()
}
