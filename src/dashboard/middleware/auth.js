export default function ({ route, redirect, store }) {
    const isLoggedIn = store.state.auth.isUserLoggedIn;
    console.log('object', isLoggedIn, route.path !== '/login');
    if (!isLoggedIn && route.path !== '/login') {
        return redirect('/login');
    }
}
