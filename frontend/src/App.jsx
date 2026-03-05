import { useEffect, useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://127.0.0.1:8000'

export default function App() {
  const [greeting, setGreeting] = useState('Loading...')
  const [error, setError] = useState('')

  useEffect(() => {
    fetch(`${API_BASE}/greeting`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`)
        }
        return response.json()
      })
      .then((data) => setGreeting(data.greeting ?? 'No greeting received'))
      .catch((err) => {
        setError(`Failed to load greeting: ${err.message}`)
        setGreeting('')
      })
  }, [])

  return (
    <main>
      <h1>Greeting from Python API</h1>
      {error ? <p className="error">{error}</p> : <p>{greeting}</p>}
    </main>
  )
}
